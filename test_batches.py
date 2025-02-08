from models import Batch, OrderLine
from datetime import date


def test_allocating_to_a_batch_reduces_the_available_quantity():
    batch = Batch("batch-001", "SMALL-TABLE", qty=20, eta=date.today())
    line = OrderLine("order-ref", "SMALL-TABLE", 2)

    batch.allocate(line)

    assert batch.available_quantity == 18

def test_cannot_allocate_if_available_smaller_than_required():
    batch = Batch("batch-001", "SMALL-TABLE", qty=10, eta=date.today())
    line = OrderLine("order-ref", "SMALL-TABLE", 12)

    assert batch.can_allocate(line) is False

def test_can_only_deallocate_allocated_lines():
    batch = Batch("batch-001", "SMALL-TABLE", qty=10, eta=date.today())
    line = OrderLine("order-ref", "RED-CHAIR", 5)

    batch.deallocate(line)
    assert batch.available_quantity == 10