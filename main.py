#!/usr/bin/env python3

# https://console.groq.com/playground

from dotenv import load_dotenv
import os
from phi.agent import Agent
from phi.model.groq import Groq
# from phi.tools.yfinance import YFinanceTools


def main():
    load_dotenv()
    foo = os.getenv('foo')
    agent = Agent(
        model=Groq(id="llama-3.3-70b-versatile")
    )
    agent.print_response("Write a 4-line poem")


if __name__ == '__main__':
    main()
