# Market Madness Algorithmic Trading Bot (2026)

This repository contains the python script that led me to a 15th place in the international DRW Market Madness 2026 Competition (https://www.drw.com/market-madness). This trading competiion was based upon the 2026 Mens NCAA Basketball tournament, commonly known as "March Madness".


# Methods:
At the start of the competition, I realized that I did not have the budget or experience to compete (in a traditional sense) with other traders, ruling out inital approaches I trialed via using sportsbook APIs or finding minute market inneficiencies. Instead, I decided that the best way to succeed in this competition was to let others make mistakes first, and capitalize on the moments when they did so. Therefore, I built a simple bot that ensured that I held a constant maximum price, maximum volume sell order on every team in the tournament with a seed rating of 9 or below. I chose 9 as the cutoff since the lowest ever seeded March Madness winner was an 8 seed. Despite the simplicity of this strategy (or perhaps because of it), I managed to snag a fair number of other traders/bots during the course of the competition. In the cases that my bot was triggered, I assume that these errors on my competitors ends were either due to market orders being placed when limit orders would have really been the more appropriate action, or that market movement on lower seeded teams after first or second round upsets caused large buy volumes for other traders/bots, resulting in them buying wildly overpriced shares in these lower seeded teams.

**Final PnL: $9,999.33**


# Future Iterations:
I intened to use this same strategy again in 2027, hopefully implementing it earlier as I did actually miss the first two days fo the 2026 tournament. I would also like to expand on the idea of letting others fail first, and perhaps set up some similar logic for teams of higher seeds.





*This project utilizes the Client infrastructure provided by DRW for the 2026 Trading Challenge, found in trading_client.py. My contribution is the trading bot implementation found in tradingbot.py.



<img width="1518" height="1347" alt="578898138-1b7061c5-061a-4be7-ac7a-ff2b4ac92360" src="https://github.com/user-attachments/assets/7feeb7c0-a561-4562-b688-5d4626ca6fde" />
