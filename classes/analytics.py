class Analytics:
    def __init__(self, snapshots, param_dict):
        self.snapshots = snapshots
        self.param_dict = param_dict
        self.zombie_snaps = []
        self.human_snaps = []
        self.time = []
        self._count_ents()
    def _count_ents(self):
        for i in range(len(self.snapshots)):
            snapshot = self.snapshots[i]
            time = (i+1)*self.param_dict["timestep"]
            no_zombies = 0
            no_humans = 0
            for ent in snapshot:
                if ent[1] == "Z":
                    no_zombies += 1
                if ent[1] == "H":
                    no_humans += 1
            self.zombie_snaps.append(no_zombies)
            self.human_snaps.append(no_humans)
            self.time.append(time)

    def __repr__(self):
        return f"{self.zombie_snaps, "\n", self.human_snaps, "\n", self.time}"


            

