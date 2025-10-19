from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

def main():
    setup(
        name='latent-diffusion',
        version='0.0.2',
        description='High-Resolution Image Synthesis with Latent Diffusion Models ',
        url='https://github.com/CompVis/latent-diffusion',
        author='Blattmann, Andreas and Rombach, Robin and Oktay, Kaan and Ommer, Björn',
        author_email='robin.rombach@gmail.com',
        packages=find_packages(),
        install_requires=required
    )

if __name__ == "__main__":
    main()