# Current goal: Experiment with vanilla DDRM to get better results

# Questions
- To evaluate the DDRM technique on street scenes for AV use case do we need to train our own diffusion model to sample from? If yes, how feasible is this? 
https://github.com/openai/improved-diffusion?
- Why might Chunming's diffusion model have no initial success?
- DDNM looks for integration friendly https://github.com/wyhuai/DDNM/blob/main/README.md

# TODO
[x] Benchmark/baseline 10 imgs from LSUN bedroom
[x] Denoise a single raindrop img 2min20s GCP 1xNvidia T4
    - Inputs to DDRM model 256 x 256 images and degradation matrix H
    - Input images are expected to reside in a 'class folder' e.g. exp2/datasets/0/img1
[X] Skip adding degradation
    [-] Update PSNR evaluation function (Not actually required). The code needs to know the where the clean image is (before noise added) for PSNR evaluation https://github.com/bahjat-kawar/ddrm/.issues/3 
[X] Denoise 10 raindrop images
    - OOM issues on GCP. Bumped to 16 cores/60GB ram. Took 20mins with 4 workers.
[X] Experiment with vanilla DDRM to get better results
[X] Modify imageNet to test hypothesis that pretrained model with more diversity = improved denoising
[ ] Create appropriate config.yml for raindrop dataset
[ ] Swap out pretrained diffusion model 
    - deep gen prior Chunming with street scenes, which only applies lin transformation
    - degrader operator still required?
    - degradation function is still necessary energy -> step
[ ] Experiment with different degradation matrix https://github.com/bahjat-kawar/ddrm/issues/5
    - Why? Because DDRM's efficient implementation relies on SVD of the degradation matrix, H which reduces time complexity from n^2 to n

# Setup
- Requires CUDA installation to match torch 1.10 or 1.8 :(
-- PyTorch 1.8: 10.1, 10.2, 11.0, 11.1
-- PyTorch 1.10 10.2, 11.1, 11.3
- clone git@github.com:jiamings/ddrm-exp-datasets.git into exp/datasets
- python main.py --ni --config bedroom.yml --doc bedroom --timesteps 20 --eta 0.85 --etaB 1 --deg sr4 --sigma_0 0.05 -i bedroom_sr4_sigma_0.05 --exp exp

# JC dataset
- raindrop https://github.com/rui1996/DeRaindrop