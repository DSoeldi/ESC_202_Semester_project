import matplotlib.pyplot as plt
import numpy as np

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
        return f"{self.zombie_snaps, self.human_snaps, self.time}"
    
    def pop_dynamics_plot(self, output_path = "outputs/pop_analytics.png" ):
        t_master = np.array(self.time) # Force to numpy for math operations

        # 1. Align time to snapshots correctly
        num_snaps = len(self.human_snaps) #how many snapshots in time
        time_indices = np.linspace(0, len(t_master) - 1, num_snaps, dtype=int)
        t_snaps_raw_hours = t_master[time_indices]

        # 2. Dynamic Time Scaling Logic (X-Axis & Values)
        actual_elapsed_h = t_snaps_raw_hours[-1]

        if actual_elapsed_h >= 1:
            time_unit = "hours"
            time_scale = 1.0
        elif (actual_elapsed_h * 60) >= 1:
            time_unit = "min."
            time_scale = 60.0
        else:
            time_unit = "sec."
            
            time_scale = 3600.0
        #scale it so we use good unit
        t_plot = t_snaps_raw_hours * time_scale 

        # --- Dictionary Formatting (Including Dynamic Timestep) ---
        sim_time_display = f"{actual_elapsed_h * time_scale:.2f} {time_unit}"

        keys_to_show = [
            "n_H", "n_Z", "timestep", "n_steps", "x_bounds", "y_bounds",
            "awareness_r_H", "awareness_r_Z", "max_speed_H", "max_speed_Z",
            "walking_speed_Z", "lonely_walk_speed_H", "H_contr_flocking",
            "bite_r_Z_H", "smooth_rand_walk"
        ]

        lines = []
        for k in keys_to_show:
            val = self.param_dict.get(k, 'N/A')
            
            if k == "n_steps":
                lines.append(f"{'sim_time':<18} | {sim_time_display}")
            
            elif k == "timestep":
                # --- NEW: Dynamic Timestep Scaling ---
                if val >= 1:
                    ts_val, ts_unit = val, "hours"
                elif (val * 60) >= 1:
                    ts_val, ts_unit = val * 60, "min."
                else:
                    ts_val, ts_unit = val * 3600, "sec."
                lines.append(f"{k:<18} | {ts_val:.2f} {ts_unit}")
                
            elif "awareness" in k or "bite" in k:
                val_m = val * 1000 if isinstance(val, (int, float)) else val
                lines.append(f"{k:<18} | {val_m:.2f} m")
                
            elif "speed" in k:
                lines.append(f"{k:<18} | {val:.2f} km/h")
                
            elif "bounds" in k:
                lines.append(f"{k:<18} | {val} km")
                
            else:
                lines.append(f"{k:<18} | {val}")

        param_text = "\n".join(lines)

        # --- Plotting ---
        fig, ax = plt.subplots(figsize=(13, 7))

        ax.plot(t_plot, self.human_snaps, color='blue', label='Humans', linewidth=2)
        ax.plot(t_plot, self.zombie_snaps, color='green', label='Zombies', linewidth=2)

        ax.set_xlabel(f'Time ({time_unit})')
        ax.set_ylabel('Number of Entities')
        ax.set_title('Human vs. Zombie Population Dynamics')
        ax.legend(loc='upper left')
        ax.grid(True, linestyle='--', alpha=0.5)

        # Text box styling
        props = dict(boxstyle='round', facecolor='white', alpha=0.9, edgecolor='lightgray')
        ax.text(1.03, 0.98, param_text, transform=ax.transAxes, fontsize=9,
                verticalalignment='top', family='monospace', bbox=props)

        plt.tight_layout(rect=[0, 0, 0.8, 1])
        plt.savefig(output_path, bbox_inches='tight', dpi=300)
        
        


            

