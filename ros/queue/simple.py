from attr import dataclass, field
from typing import Optional


@dataclass
class SimpleQueue:
    # General
    name: str
    target: str
    max_limit: str = "0/0"
    dst: Optional[str] = None
    burst_limit: str = None
    burst_threshold: str = None
    burst_time: str = None
    time: str = None
    disabled: bool = False
    comment: Optional[str] = None
    # Advanced
    packet_marks: Optional[str] = None
    limit_at: str = "0/0"
    priority: str = "8/8"
    bucket_size: str = "0.100/0.100"
    queue: Optional[str] = None
    parent: Optional[str] = None
    # Total
    total_bucket_size: Optional[str] = None
    total_burst_threshold: Optional[str] = None
    total_limit_at: Optional[str] = None
    total_priority: Optional[int] = None
    total_burst_limit: Optional[str] = None
    total_burst_time: Optional[str] = None
    total_max_limit: Optional[str] = None
    total_queue: Optional[str] = None
    # Statistics
    rate: str = field(on_setattr=None, default=None)
    packet_rate: str = field(on_setattr=None, default=None)
    queued_bytes: str = field(on_setattr=None, default=None)
    queued_packets: str = field(on_setattr=None, default=None)
    bytes: str = field(on_setattr=None, default=None)
    packets: str = field(on_setattr=None, default=None)
    dropped: str = field(on_setattr=None, default=None)
    pcq_queues: Optional[str] = field(on_setattr=None, default=None)
    # Total Statistics
    total_rate: str = field(on_setattr=None, default=None)
    total_packet_rate: int = field(on_setattr=None, default=None)
    total_queued_bytes: str = field(on_setattr=None, default=None)
    total_queued_packets: int = field(on_setattr=None, default=None)
    total_bytes: str = field(on_setattr=None, default=None)
    total_packets: int = field(on_setattr=None, default=None)
    total_dropped: int = field(on_setattr=None, default=None)
    total_pcq_queues: Optional[str] = field(on_setattr=None, default=None)
    # ETC
    id: str = field(on_setattr=None, default=None)
    dynamic: bool = field(on_setattr=None, default=None)
    invalid: bool = field(on_setattr=None, default=None)

    def __str__(self) -> str:
        return self.name

    def __bool__(self) -> bool:
        return not self.disabled
