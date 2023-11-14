# Current goal: skip adding degradation
- Inputs to DDRM model 256 x 256 images and degradation matrix H
- Input images need to reside in a 'class folder' e.g. exp2/datasets/0/img1
- raindrop dataset https://github.com/rui1996/DeRaindrop

# TODO
[x] Denoise a single raindrop img 2min20s GCP 1xNvidia T4
[X] Skip adding degradation
    [ ] Update PSNR evaluation function. The code needs to know the where the clean image is (before noise added) for PSNR evaluation https://github.com/bahjat-kawar/ddrm/issues/3 
[ ] Denoise 10 raindrop images
    - OOM issues on GCP
[ ] Create appropriate config.yml for raindrop dataset 
[ ] Swap out pretrained diffusion model 
[ ] Experiment with different degradation matrix https://github.com/bahjat-kawar/ddrm/issues/5
    - Why? Because DDRM's efficient implementation relies on SVD of the degradation matrix, H which reduces time complexity from n^2 to n

# Setup
- Requires CUDA installation to match torch 1.10 or 1.8 :(
-- PyTorch 1.8: 10.1, 10.2, 11.0, 11.1
-- PyTorch 1.10 10.2, 11.1, 11.3
- clone git@github.com:jiamings/ddrm-exp-datasets.git into exp/datasets
- python main.py --ni --config bedroom.yml --doc bedroom --timesteps 20 --eta 0.85 --etaB 1 --deg sr4 --sigma_0 0.05 -i bedroom_sr4_sigma_0.05 --exp exp