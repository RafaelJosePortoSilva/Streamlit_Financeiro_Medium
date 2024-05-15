import streamlit as st
import yfinance as yf

def main():
    symbol = 'PETR4.SA'
    petra = yf.Ticker(symbol)
    data = petra.history('1mo')
    atual = data.iloc[1,:]

    close = atual.Close
    delta = atual.Close - atual.Open 

    st.title('Teste')
    st.metric(
        label = 'Petr4.SA',
        value = close,
        delta = delta
    )



if __name__ == '__main__':
    main()