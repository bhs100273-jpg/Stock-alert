import json, urllib.request, urllib.parse, datetime, time
symbols=["005930.KS","AAPL","AVGO","ABBV","AMZN","BRK-B","GOOG","GOOGL","LLY","MSFT","NFLX","TSM","NVDA"]
names=["삼성전자","애플","브로드컴","애브비","아마존","버크셔 해서웨이 B","알파벳 C","알파벳 A","일라이 릴리","마이크로소프트","넷플릭스","TSMC ADR","엔비디아"]
markets=["국내"]+["미국"]*12
curr=["KRW"]+["USD"]*12
out=[]
for sym,name,market,currency in zip(symbols,names,markets,curr):
    url="https://query1.finance.yahoo.com/v8/finance/chart/"+urllib.parse.quote(sym)+"?range=2d&interval=1d"
    req=urllib.request.Request(url,headers={"User-Agent":"Mozilla/5.0"})
    with urllib.request.urlopen(req,timeout=15) as f: d=json.load(f)
    m=d["chart"]["result"][0]["meta"]
    price=float(m.get("regularMarketPrice") or m.get("previousClose"))
    prev=float(m.get("chartPreviousClose") or m.get("previousClose"))
    out.append({"name":name,"symbol":sym,"market":market,"currency":currency,"price":price,"prev":prev,"percent":(price/prev-1)*100 if prev else 0})
    time.sleep(.15)
with open("data.json","w",encoding="utf-8") as f:
    json.dump({"updatedAt":datetime.datetime.now(datetime.timezone.utc).isoformat(),"stocks":out},f,ensure_ascii=False,indent=2)
