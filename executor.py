class Executor:
    def execute(self, opportunity, size, dry_run=True):
        if dry_run:
            return {"status":"dry_run","pair_cost":opportunity.pair_cost,"edge":opportunity.edge,"size":size}
        raise NotImplementedError("Production execution is intentionally excluded.")
