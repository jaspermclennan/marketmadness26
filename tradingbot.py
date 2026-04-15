import aiohttp
import asyncio
from trading_client import Client, create_session


class TradingBot(Client):
    def __init__(
        self,
        session: aiohttp.ClientSession,
        game_id: int,
        token: str,
    ) -> None:
        super().__init__(session, game_id, token)
        
        
    async def on_start(self) -> None:


        while True:

##############################################Trading Bot START##########################################################################################
        # Define the 9-16 seed targets that I wanted to "short"
            underdogs = [
                    
                # 8 Seeds (The 50/50 toss-ups)
                "Ohio State", "Georgia", "Clemson", "Villanova",
                # 9 Seeds
                "Iowa", "Saint Louis", "Utah St", "TCU",
                # 10 Seeds
                "Texas A&M", "Santa Clara", "Missouri", "UCF",
                # 11 Seeds (Includes First Four teams)
                "VCU", "Miami OH", "SMU", "NC State", "South Florida", #"Texas" was removed due to manual buy upset possible agaisnt BYU
                # 12 Seeds
                "McNeese", "Akron", "High Point", "Northern Iowa",
                # 13 Seeds
                "Troy", "Hofstra", "Hawaii", "Cal Baptist",
                # 14 Seeds
                "Penn", "Wright St", "Kennesaw St", "North Dakota St",
                # 15 Seeds
                "Idaho", "Tennessee St", "Queens", "Furman",
                # 16 Seeds (Includes First Four teams)
                "Prairie View", "Lehigh", "UMBC", "Howard", "Long Island", "Siena"
            ]
            
            

            # Refresh my current positions from DRW 
            await self.update_positions()
            current_orders = await self.get_open_orders()

            # Check each team and maintain the -100 short at 64.00
            for team in underdogs:
                pos = self.positions.get(team, 0)
                pending = sum(o.qty for o in current_orders.values() 
                             if o.display_symbol == team and o.px == 64.0)
                
                # If (Current Position + Waiting Orders) isn't -100, fill the gap
                needed = -100 - (pos + pending)

                if needed < 0:
                    try:
                        await self.send_order(team, 64.00, needed, "LIMIT")
                    except:
                        pass # Ignore if margin limit is hit
            
            
            
#############################################Trading Bot END##########################################################################################


            await asyncio.sleep(1)



async def main():
    async with create_session() as session:
        client = TradingBot(session, game_id, token)
        print(f"Access web view at {client.web_url}")
        await client.start()


await main()
