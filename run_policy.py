from utils.sys_run import PolicyRunner
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'
runner = PolicyRunner(
    log_policy_dir_list=["/home/rtu/gym_plaground/DSAC-v2/results/DSAC_V2_gym_bipedalwalkerhardcore/251126-074140"],
    trained_policy_iteration_list=["40000"],
    is_init_info=False,
    init_info={"init_state": [-1, 0.05, 0.05, 0, 0.1, 0.1]},
    save_render=True,
    legend_list=["DSAC_V2"],
    dt=0.01, # time interval between steps
)

runner.run()
