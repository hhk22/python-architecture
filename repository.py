
import abc
import models
from sqlalchemy.orm import Session

class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, batch: models.Batch):
        raise NotImplementedError
    
    @abc.abstractmethod
    def get(self, reference: str) -> models.Batch:
        raise NotImplementedError


class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session: Session):
        self.session = session
    
    def add(self, batch: models.Batch):
        self.session.add(batch)
    
    def get(self, reference: str):
        return self.session.query(models.Batch).filter_by(reference=reference).one()

    def list(self):
        return self.session.query(models.Batch).all()