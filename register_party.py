import pandas as pd
def register_paryt():
    
    List_of_parties={"party_name":["ASC","ATM","AASD","ANC","AGANSA","ALJAMA","ATA","AZAPO","APC","BRA","BLF","ZACP","CPM","CSA","COPE","DA","DLC","ECOFORUM","EFF","F4SD","FREE DEMS"],
                     "reg_number":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21],
                     "member_count":[1200,1000,145,134,2333,89,5600,9000,7890,234,5678,8000,78000,90000,67000,5678,890,78,89,899,12]}
    
    df=pd.DataFrame(List_of_parties)
    
    """if df[df["member_count"]]>1000:
        filter=df[df["paryt_name"]]"""
        
register_paryt()        
    
    