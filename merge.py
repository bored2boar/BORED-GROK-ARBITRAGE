class PositionMerger:
    def merge(self, market_id, size, dry_run=True):
        if dry_run:
            return {"status":"dry_run","market_id":market_id,"size":size}
        raise NotImplementedError("Production settlement infrastructure is intentionally excluded.")
