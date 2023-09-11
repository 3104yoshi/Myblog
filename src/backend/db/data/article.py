from dataclasses import dataclass
import datetime

@dataclass
class article:
    articleId: int
    title: str
    content: str
    updateDate: datetime

    def __init__(self, articleId, title, content):
        self.articleId = articleId
        self.title = title
        self.content = content
        self.updateDate = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")