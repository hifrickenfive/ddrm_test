# Setup
- Requires CUDA installation to match torch 1.10 or 1.8 :(
-- PyTorch 1.8: 10.1, 10.2, 11.0, 11.1
-- PyTorch 1.10 10.2, 11.1, 11.3
- clone git@github.com:jiamings/ddrm-exp-datasets.git into exp/datasets
- python main.py --ni --config bedroom.yml --doc bedroom --timesteps 20 --eta 0.85 --etaB 1 --deg sr4 --sigma_0 0.05 -i bedroom_sr4_sigma_0.05 --exp exp

# Inputs to DDRM model
- 256 x 256 images
- degradation matrix H

# To what extent is adverse weather a linear inverse problem?
- medical imaging is...
- not car video cameras because 1) non-linear weather effects, 2) non linearity in camera sensors, e.g. sensitivity to light, 3) diversity of adverse weather conditions

# Problem: cannot take in blurry image into the model to clean it https://github.com/bahjat-kawar/ddrm/issues/3 
Changes required
- the code requires the original image for PSNR evaluation
- you also need to make sure the code uses the correct blurring kernel

# Problem: DDRM relies on pretrained diffusion models https://github.com/bahjat-kawar/ddrm/issues/6
Changes required
- Either get an existing pretrained weather diffusion model or train our own one https://github.com/openai/guided-diffusion 256x256 diffusion model is 2GB
Question
- How are the pretrained models used?

# Problem: DDRM relies on a known H degradation matrix https://github.com/bahjat-kawar/ddrm/issues/5
- Why? Because its efficient implementation relies on SVD of the degradation matrix, H which reduces time complexity from n^2 to n
