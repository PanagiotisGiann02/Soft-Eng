# hiking_buddy/core/repositories/trash_report_repository.py

from domain.models.trashReport import TrashReport


class TrashReportRepository:
    def get_next_id(self) -> int:
        raise NotImplementedError

    def save(self, report: TrashReport) -> None:
        raise NotImplementedError


class InMemoryTrashReportRepository(TrashReportRepository):
    def __init__(self):
        self.reports = {}
        self.current_id = 1

    def get_next_id(self) -> int:
        next_id = self.current_id
        self.current_id += 1
        return next_id

    def save(self, report: TrashReport) -> None:
        self.reports[report.id] = report
        print(f"[TrashReportRepository] TrashReport {report.id} saved.")
