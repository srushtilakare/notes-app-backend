from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app import models, schemas
from app.auth import get_current_user

router = APIRouter()


# CREATE NOTE
@router.post("/notes", response_model=schemas.NoteResponse)
def create_note(
    note: schemas.NoteCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):

    new_note = models.Note(
        title=note.title,
        content=note.content,
        owner_id=current_user.id
    )

    db.add(new_note)
    db.commit()
    db.refresh(new_note)

    return new_note

# GET ALL NOTES
@router.get("/notes", response_model=list[schemas.NoteResponse])
def get_all_notes(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):

    notes = db.query(models.Note).filter(
        models.Note.owner_id == current_user.id
    ).all()

    return notes

# GET NOTE BY ID
# GET NOTE BY ID
@router.get("/notes/{note_id}", response_model=schemas.NoteResponse)
def get_note_by_id(
    note_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):

    # Check ownership
    note = db.query(models.Note).filter(
        models.Note.id == note_id
    ).first()

    if not note:
        raise HTTPException(
            status_code=404,
            detail="Note not found"
        )

    # Owner access
    if note.owner_id == current_user.id:
        return note

    # Shared access
    shared = db.query(models.SharedNote).filter(
        models.SharedNote.note_id == note.id,
        models.SharedNote.user_id == current_user.id
    ).first()

    if shared:
        return note

    raise HTTPException(
        status_code=403,
        detail="Access denied"
    )

# UPDATE NOTE
@router.put("/notes/{note_id}", response_model=schemas.NoteResponse)
def update_note(
    note_id: int,
    updated_note: schemas.NoteCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):

    note = db.query(models.Note).filter(
        models.Note.id == note_id,
        models.Note.owner_id == current_user.id
    ).first()

    if not note:
        raise HTTPException(
            status_code=404,
            detail="Note not found"
        )

    note.title = updated_note.title
    note.content = updated_note.content

    db.commit()
    db.refresh(note)

    return note

# DELETE NOTE
@router.delete("/notes/{note_id}")
def delete_note(
    note_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):

    note = db.query(models.Note).filter(
        models.Note.id == note_id,
        models.Note.owner_id == current_user.id
    ).first()

    if not note:
        raise HTTPException(
            status_code=404,
            detail="Note not found"
        )

    db.delete(note)
    db.commit()

    return {
        "message": "Note deleted successfully"
    }

# SHARE NOTE
@router.post("/notes/{note_id}/share")
def share_note(
    note_id: int,
    share_data: schemas.ShareNote,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):

    # Find note
    note = db.query(models.Note).filter(
        models.Note.id == note_id,
        models.Note.owner_id == current_user.id
    ).first()

    if not note:
        raise HTTPException(
            status_code=404,
            detail="Note not found"
        )

    # Find user to share with
    target_user = db.query(models.User).filter(
        models.User.email == share_data.share_with_email
    ).first()

    if not target_user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    # Prevent sharing with self
    if target_user.id == current_user.id:
        raise HTTPException(
            status_code=400,
            detail="Cannot share note with yourself"
        )

    # Check if already shared
    existing_share = db.query(models.SharedNote).filter(
        models.SharedNote.note_id == note.id,
        models.SharedNote.user_id == target_user.id
    ).first()

    if existing_share:
        raise HTTPException(
            status_code=400,
            detail="Note already shared with this user"
        )

    # Create shared record
    shared_note = models.SharedNote(
        note_id=note.id,
        user_id=target_user.id
    )

    db.add(shared_note)
    db.commit()

    return {
        "message": f"Note shared with {target_user.email}"
    }