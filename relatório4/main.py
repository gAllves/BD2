from productAnalyzer import ProductAnalyzer
from database import Database

db = Database(database="mercado", collection="compras")
db.resetDatabase()

productAnalyzer = ProductAnalyzer("mercado", "compras")

productAnalyzer.vendasdia()
productAnalyzer.produtomaisvendido()
productAnalyzer.clientemais()
productAnalyzer.produtos1()