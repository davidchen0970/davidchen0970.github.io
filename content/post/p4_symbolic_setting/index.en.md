+++
date = '2024-11-05T02:35:09+08:00'
title = 'P4 Troubleshooting - Symbolic Link'
image = "pawel-czerwinski-8uZPynIu-rQ-unsplash.jpg"
categories = [
    "P4"
]
+++

# P4 Troubleshooting - Symbolic Link

When working with the P4 tutorials, we can typically run the `make run` command without issues. However, if we move outside of the tutorial directory, we might find that the `make run` command stops working, usually due to an error like this:

```bash!=
Makefile:4: ../../utils/Makefile: No such file or directory
make: *** No rule to make target '../../utils/Makefile'.  Stop
```

This error indicates that the `Makefile` cannot be found, so `make run` fails to execute. To address this, one solution is to use a symbolic link to create the necessary path, allowing the system to locate the required `Makefile` without altering the existing project structure.

## Using Symbolic Links to Fix Makefile Path Issues

By creating a symbolic link, you can point to an existing `Makefile` and resolve the “file not found” issue. This method is flexible, allowing you to fix path issues while keeping the original project structure intact.

### Steps

1. **Identify a Valid Makefile Path**: First, locate a usable `Makefile`, typically in a different project directory or a related folder.

2. **Navigate to the Target Directory**: Enter the directory where the `make` command expects the file, such as `../../utils/`.

3. **Create the Symbolic Link**: Use the `ln -s` command to create the symbolic link. Here’s the syntax:

   ```bash
   ln -s /path/to/existing/Makefile Makefile
   ```

   For example, if the valid `Makefile` is located at `/home/p4/tutorials/utils`, you would run:

   ```bash
   ln -s /home/p4/tutorials/utils ../../utils
   ```

4. **Verify the Symbolic Link**: After creating the link, use this command to check that it correctly points to the `Makefile`:

   ```bash
   ls -l ../../utils/Makefile
   ```

   If successful, Linux will return something like `w-r-- 1 ...`, confirming that the system has located the file, and you should be able to use `make run` again.

5. **Additional Errors**

   ```bash!=
   - ERROR! While parsing input runtime configuration: file does not exist /home/p4/Desktop/tutorials/basic/build/basic.p4.p4info.txtpb
   Configuring switch s2 using P4Runtime with file pod-topo/s2-runtime.json
   - ERROR! While parsing input runtime configuration: file does not exist /home/p4/Desktop/tutorials/basic/build/basic.p4.p4info.txtpb
   Configuring switch s3 using P4Runtime with file pod-topo/s3-runtime.json
   - ERROR! While parsing input runtime configuration: file does not exist /home/p4/Desktop/tutorials/basic/build/basic.p4.p4info.txtpb
   Configuring switch s4 using P4Runtime with file pod-topo/s4-runtime.json
   ```

   This error might stem from a file name or path configuration issue. Here are some solutions to resolve it:

   1. Check and retry the compilation parameters (adjust for your specific P4 program as needed):

   ```bash!=
   p4c-bm2-ss --p4v 16 --p4runtime-files build/basic.p4.p4info.txt -o build/basic.json basic.p4
   ```

   2. Update Configuration Files to Use `.txt` Format:
      Ensure that all configuration files referencing the `p4info` file use the `.txt` extension, updating paths in files like `pod-topo/s1-runtime.json` to `build/basic.p4.p4info.txt`.

   3. Rerun `make run`:
      Once files are generated, try running `make run` again to see if the switches configure correctly.

   These steps should address the `.txtpb` format issues, allowing the compiler to generate the `p4runtime` files successfully.

```

```
