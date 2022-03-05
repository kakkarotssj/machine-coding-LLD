from enum import Enum


class OrderStatuses(Enum):
    PLACED = 'PLACED'
    CONFIRMED = 'CONFIRMED'
    IN_TRANSIT = 'IN_TRANSIT'
    DELIVERED = 'DELIVERED'
    CANCELLED = 'CANCELLED'
