import sys
import os
import mnempy


def get_cmd_line():
    """Extract the app command line from sys.argv.

    :return: The command and any arguments for it that are to be sent to the
    app.
    :rtype: str
    """
    # If the user has entered any commands for the app, they are all the
    # elements of sys.argv that are after the script name.
    # Normally the script will be run with a command like "python script.py",
    # and the script name will simply be sys.argv[0]. But there are some
    # exceptions. The command line might be sent as a command-line argument
    # to a separate script, such as a testing script, in which case the script
    # name we want will be at argv[1] or later.
    # The script name can appear in different forms. It might appear as only
    # the filename or as the full path. To avoid testing for both and dealing
    # with OS separators, let's assume a string that ends with the filename
    # might be the expected script name.
    script_name = os.path.basename(__file__)
    # The script name can also be '-c' if the Python interpreter was run with
    # that option. It can be the empty string if the interpreter was given
    # no script name.
    # It's convenient to get the script name index by finding the script name
    # and then finding its index, which suggests a list comprehension.
    argv_scripts = [arg for arg in sys.argv
                    if arg.endswith(script_name) or arg in ['-c', '']]
    # We'll return None if there are no elements after the script name.
    line = None
    if len(argv_scripts) > 0:
        # We're assuming the first element that matches a script name
        # argument is the script name we expect from an argv.
        argv_script = argv_scripts[0]
        script_index = sys.argv.index(argv_script)
        if len(sys.argv) > script_index + 1:
            # cmd will parse the line itself, so we'll give it the arguments
            # as a single string.
            line = ' '.join(sys.argv[script_index + 1:])
    return line


def main():
    cli = mnempy.cli.CLI()

    line = get_cmd_line()
    if line:
        return cli.onecmd(line)
    else:
        cli.cmdloop()


if __name__ == '__main__':
    main()
