import streamlit as st
import yfinance as yf
st.title("Stock Price Tracker")
def stock_details(stock):
    ticker=yf.Ticker(stock)
    info=ticker.info
    name=info.get("longName","N/A")
    price=info.get("currentPrice","N/A")
    market_cap=info.get("marketCap","N/A")
    dividend=info.get("dividendYield","N/A")
    logo_url=info.get("logo_url","N/A")
    hist=ticker.history(period="1y")
    return{
        "Name":name,
        "Market Cap":market_cap,
        "Dividend Yield":dividend,
        "Current Price":price,
        "Logo":logo_url,
        "History":hist
    }
stock=st.text_input("Enter stock ticker...")
symbol=st.button("Search")
if symbol:
    if stock:
        details=stock_details(stock)
        st.write(f"Details for {stock}:")
        st.write(f"Name: {details['Name']}")
        st.write(f"Market Cap: {details['Market Cap']}")
        st.write(f"Dividend Yield: {details['Dividend Yield']}")
        st.write(f"Current Price: {details['Current Price']}")
        if details["Logo"]!="N/A":
            st.image(details['Logo'], width=100) 
        else:
            st.write("Logo not available")
        st.line_chart(details['History']['Close'])
    else:
        st.write("Please enter a valid stock ticker.") 