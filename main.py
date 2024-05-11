# https://medium.com/@matheuspereira_94841/criando-um-dashboard-interativo-com-streamlit-em-python-7374fe4aa8c6

import streamlit as st
import yfinance as yf

def main():
    st.title('Dashboard Financeiro')
    symbol = 'PETR4.SA'
    data = yf.download(symbol, start="2022-01-01", end="2022-12-31")
    st.line_chart(data)

    st.header(f'Tabela de Preços - {symbol}')
    st.write(data)


if __name__ == '__main__':
    main()