import requests

class CookieException(Exception):
    pass

class StockInfo:
    def __init__(self,json) -> None:
        data = json["StockInfo"]
        self.id:int = data["Commkey"]
        self.name:str = data["Name"]
        self.marketType:int = data["MarketType"]
        self.refPrice:float = data["RefPrice"]
        self.ceilPrice:float = data["CeilPrice"]
        self.floorPrice:float = data["FloorPrice"]
        self.salePrice:float = data["SalePrice"]
        self.totalQty:int = data["TotalQty"]
        self.demicalPoints:float = data["DecimalPoint"]
        self.lowPr:float = data["LowPr"]
        self.isWarrant:bool = json["IsWarrant"]


class Client:
    """
    # The Client
    ## parameters
    - cookie:cookie file location (txt,utf-8)

    ## Fow now, only stocks are supported
    """
    def __init__(self,cookie) -> None:
        self.id = ""
        self.header = ""
        try:
            with open(cookie,"r",encoding="utf-8") as c:
                self.header = {
                    "Cookie":c.read()
                }
        except:
            raise CookieException("Can't find or read cookie file")
        
    def get_price(id:int) -> StockInfo:
        json = requests.get(f"https://www.cmoney.tw/vt/ashx/HandlerGetStockPrice.ashx?q={id}&accountType=7&isSDAndSell=false").json()
        return StockInfo(json)