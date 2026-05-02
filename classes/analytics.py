class Analytics:
    def __init__(self, snapshots, param_dict):
        self.snapshots = snapshots
        self.zombie_snaps = []
        self.human_snaps = []
    def _count_ents(self):
        for snapshot in self.snapshots:
            no_zombies = 0
            no_humans = 0
            for ent in snapshot:
                if ent[1] == "Z":
                    no_zombies += 1
                if ent[1] == "H":
                    no_humans += 1

            

