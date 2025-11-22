# tikkun_abramelin.py
# Michael Joyce + Grok — 17 Nov 2025
import json
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import random
import os

class AbramelinSquare:
    def __init__(self, name, purpose, grid):
        self.name = name
        self.purpose = purpose
        self.grid = np.array(grid)

    def visualize(self):
        fig, ax = plt.subplots(figsize=(12,12))
        ax.set_facecolor('#0d0d0d')
        fig.patch.set_facecolor('#0d0d0d')

        # Radiant gold grid
        for i in range(len(self.grid)+1):
            ax.axhline(i-0.5, color='#ffd700', linewidth=5, alpha=0.9)
            ax.axvline(i-0.5, color='#ffd700', linewidth=5, alpha=0.9)

        # Glowing letters
        for (i, j), letter in np.ndenumerate(self.grid):
            ax.text(j, i, letter, ha='center', va='center',
                    fontsize=42, fontweight='bold', color='#ffaa00',
                    bbox=dict(boxstyle="round,pad=1.2", facecolor="#000000", 
                              edgecolor="#ffd700", linewidth=4, alpha=0.95))

        # AEST time only (no astropy moon)
        aest_time = datetime.now().astimezone()
        time_str = aest_time.strftime("%d %B %Y • %I:%M %p AEST")
        ax.set_title(f"{self.name}\n{self.purpose}\n{time_str}", 
                     fontsize=22, color='#ff6b6b', pad=60, fontfamily='serif')

        ax.axis('off')
        plt.tight_layout()

        if not os.path.exists("../talismans"):
            os.makedirs("../talismans")
        filename = f"../talismans/talisman_{self.purpose.replace(' ','_')}_{aest_time.strftime('%Y%m%d_%H%M')}_AEST.png"
        plt.savefig(filename, dpi=400, bbox_inches='tight', facecolor='#0d0d0d')
        print(f"Talisman forged: {filename}")
        plt.show()

class TikkunAbramelin:
    def __init__(self):
        self.squares = self.built_in_squares()
        print(f"Tikkun Abramelin Engine • {len(self.squares)} squares loaded • {datetime.now().strftime('%d %B %Y')}")

    def built_in_squares(self):
        return [
            AbramelinSquare("MOREHORIRERINIRERIROROM", "To Know Things Past",
                [["M","O","R","E","H"], ["O","R","E","H","O"], ["R","E","H","O","R"], ["E","H","O","R","E"], ["H","O","R","E","M"]]),
            AbramelinSquare("NABHIADA IH BARABHIADA IHBA N", "To Know Future Things",
                [["N","A","B","H","I"], ["A","B","H","I","A"], ["B","H","I","A","D"], ["H","I","A","D","A"], ["I","A","D","A","I"]])
        ]

    def invoke(self, purpose):
        matches = [s for s in self.squares if purpose.lower() in s.purpose.lower()]
        if not matches:
            print("No square found. Try: past, future")
            return
        square = random.choice(matches)
        print(f"\nInvoking: {square.name} — {square.purpose}")
        square.visualize()

if __name__ == "__main__":
    engine = TikkunAbramelin()
    purpose = input("\nWhat do you seek tonight? → ").strip()
    engine.invoke(purpose)