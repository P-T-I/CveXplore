from CveXplore.update.Sources_process import (
    CPEDownloads,
    CVEDownloads,
    CWEDownloads,
    CAPECDownloads,
    VIADownloads,
    DatabaseIndexer,
)


class MainUpdater(object):
    def __init__(self, repopulate=False):

        self.repopulate = repopulate

        self.sources = [
            {"name": "cpe", "updater": CPEDownloads},
            {"name": "cve", "updater": CVEDownloads},
            {"name": "cwe", "updater": CWEDownloads},
            {"name": "capec", "updater": CAPECDownloads},
            {"name": "via4", "updater": VIADownloads},
        ]

        self.posts = [{"name": "ensureindex", "updater": DatabaseIndexer}]

    def update(self):

        for source in self.sources:
            up = source["updater"]()
            up.update()

        for post in self.posts:
            indexer = post["updater"]()
            indexer.create_indexes()

    def populate(self):

        for source in self.sources:
            populator = source["updater"]()
            populator.populate()

        for post in self.posts:
            indexer = post["updater"]()
            indexer.create_indexes()
