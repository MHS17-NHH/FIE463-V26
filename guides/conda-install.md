# Installing the Anaconda Python distribution

- Anaconda is a distribution that includes both Python and numerous packages
  for scientific computing. 
- You should prefer Anaconda over a "bare minimum" Python installer
  such as the one distributed via [python.org](https://www.python.org/downloads/).
- You should prefer Anaconda over the Python distribution shipped with
  your operating system (macOS and Linux).

## Installation

1. Download the installer from the [Anaconda website](https://www.anaconda.com/download/success).
    - **No registration is required**; skip it if prompted.
    - You need to choose the correct installer for your platform.
    - For macOS, this depends on your hardware (*Apple Silicon* or *Intel*).
      If you are unsure which you have, consult 
      [this guide](https://support.apple.com/guide/mac-help/get-system-information-about-your-mac-syspr35536/mac).
2. Running the installer should be straightforward, but you can consult
    [this guide](https://docs.anaconda.com/anaconda/install/) 
    if needed.

## Creating an Anaconda environment

-   The Anaconda installation comes with a default environment called `base`
    which contains most if not all packages required for this course.
-   Nevertheless, you should create a course-specific environment
    from the environment definition file [`environment.yml`](../environment.yml).

    This has the advantage that the Python and package versions you use 
    are the same as those used by the instructor.

To create the environment, you can use *one* of the following alternatives:

1. Creating the environment using the `environment.yml` file on your computer:
    
    -   Open the Anaconda Prompt (Windows) or the terminal (macOS, Linux)
        and change to the folder where you cloned the course repository 
        (the one that contains `environment.yml`):

        On Windows, use something like:
        ```cmd
        cd "c:\Users\username\path\to\FIE463-V26"
        ```

        On macOS or Linux, use something like:
        ```bash
        cd "/Users/username/path/to/FIE463-V26"
        ```

    -   Run the following command:
        ```bash
        conda env create -f environment.yml
        ```

2.  Creating the environment using the `environment.yml` file from GitHub directly 
    (if you are unsure where `environment.yml` is located on your system):
    
    -   Open the Anaconda Prompt (Windows) or the terminal (macOS, Linux) and run the following commands:
        ```bash
        curl -O https://raw.githubusercontent.com/richardfoltyn/FIE463-V26/main/environment.yml
        conda env create -f environment.yml
        ```

If everything worked out, you should see the following message at the end of the output:
```bash
# To activate this environment, use
#
#     $ conda activate FIE463
#
# To deactivate an active environment, use
#
#     $ conda deactivate

```

### Note for macOS users on Intel chips

- Apple and Anaconda have 
   [terminated support](https://www.anaconda.com/blog/intel-mac-package-support-deprecation) 
   for Intel-based Macs,
   and hence some of the packages in `environment.yml` may not be
   available for your platform.

- There is an alternative environment definition file 
   [`environment-intel-mac.yml`](../environment-intel-mac.yml) 
   for such cases. Create the environment as follows:
    ```bash
    conda env create -f environment-intel-mac.yml
    ```
- Note that some packages will be outdated and may be missing some 
  of the features we use in the course.