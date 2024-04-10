import rerun as rr  # NOTE: `rerun`, not `rerun-sdk`!
import numpy as np

# Initialize the rerun sdk
rr.init("rerun_example")

# Connect to a rerun viewer on a remote machine (the server)
rr.connect(addr="10.136.196.221:9876")

SIZE = 10

pos_grid = np.meshgrid(*[np.linspace(-10, 10, SIZE)]*3)
positions = np.vstack([d.reshape(-1) for d in pos_grid]).T

col_grid = np.meshgrid(*[np.linspace(0, 255, SIZE)]*3)
colors = np.vstack([c.reshape(-1) for c in col_grid]).astype(np.uint8).T

rr.log(
    "my_points",
    rr.Points3D(positions, colors=colors, radii=0.5)
)
