from modules.view import TubeTuneApp
from modules.controller import TubeTuneController
from modules.model import YTDownloadManager


if __name__ == "__main__":
    model = YTDownloadManager()
    app = TubeTuneApp(400, 250)
    controller = TubeTuneController(app, model)
    
    app.run()
