"""
All functions are already written in the code, except for `auto_missions`, I'm letting this at the disposal of all, 
those who wants to counterfeit is free to submit his changes, the aim is to complete as many of the current celebration's missions as possible.
For example, use 500 STA, complete a dokkan event 10 times, LR campains ...
"""

class DOKKAN:
    
    def __init__(self):
        pass
    
    def auto_missions(self):
        """
        Auto mission class, I'm letting this at the disposal of all, 
        those who wants to counterfeit is free to submit his changes.
        You're free to print your name as contributor (use function `colmsg` to print).
        """
        
        # ==========================================================
        #                       Code Here   
        #                       Example :
        self.accept_gifts()
        self.complete_area('720') # --> SBR area
        self.complete_clash()
        self.complete_stage('720001', auto_update_team=True, limitation=None, difficulty=None, kagi=None, repeat=10) # --> Clears SBR stage 10 times
        self.accept_missions()
        # ==========================================================
        
        pass
        

    def accept_gifts(self):
        """
        Accept gifts
        """
        return
        
    def accept_missions(self):
        """
        Accept missions
        """
        return

    def complete_stage(self, stage_id, auto_update_team=True, limitation=None, difficulty=None, kagi=None, repeat=1):
        """
        stage_id : String
        auto_update_team : Enable or not auto update
        limitation : If there's a limitation on the event, leave at NONE and the function will look if there's a limitation by itself
        difficulty : If difficulty is not given, completes the highest difficulty
        kagi: set to True if it is a key event
        repeat : number of time the stage should be done.
        """
        return
    
    def complete_area(self, area_id):
        """
        area_id : String
        """
        return
    
    def complete_clash(self):
        """
        Completes Battle Royale if there's one.
        """
        return
    
    def auto_sell_cards(self):
        """
        Sells useless cards from story mode and zeni statues
        """
        return
        
def colmsg(color_code, message, style=None, bg_color=None):
    """
    function to print colored message in console.
    """
    color_map = {
        'red': Fore.RED,
        'green': Fore.GREEN,
        'blue': Fore.BLUE,
        'yellow': Fore.YELLOW,
        'cyan': Fore.CYAN,
        'magenta': Fore.MAGENTA,
        'white': Fore.WHITE,
    }

    bg_color_map = {
        'black': Back.BLACK,
        'red': Back.RED,
        'green': Back.GREEN,
        'yellow': Back.YELLOW,
        'blue': Back.BLUE,
        'magenta': Back.MAGENTA,
        'cyan': Back.CYAN,
        'white': Back.WHITE,
    }

    style_map = {
        'reset': Style.RESET_ALL,
        'bold': Style.BRIGHT,
        'dim': Style.DIM,
    }
    pass