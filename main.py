import os
import datetime
import sys
import string
from script import Script
from colors import Colors
from runtime import se

start = datetime.datetime.now()

# Create scripts folder if it doesn't exist
if not os.path.exists("scripts"):
    os.makedirs("scripts")

# Initialize output
output = None

# Execute scripts
if len(sys.argv) > 1:
    filename = sys.argv[1]
    if filename.endswith(".ff"):
        print("Running .. .. ..")
        with open(sys.argv[1], encoding='utf-8') as file:
            output = se(sys.argv[1], ''.join(string.digits + string.ascii_lowercase))
            s = Script(file)
            s.run()
            print("\n\n")
    else:
        print("[@] Please use extension `.ff` for fangs codefiles. \nNot a FANGS codefile but still, running .. .. ..")
        with open(sys.argv[1], encoding='utf-8') as file:
            output = se(sys.argv[1], ''.join(string.digits + string.ascii_lowercase))
            s = Script(file)
            s.run()
            print("\n\n")
   
else:
    pass
    # for filename in os.listdir("scripts"):
    #     if filename.endswith(".ff"):
    #         with open(os.path.join("scripts", filename), encoding='utf-8') as file:
    #             output = se(filename, ''.join(string.digits + string.ascii_lowercase))
    #             s = Script(file)
    #             s.run()
    #     else:
    #         print("[@] Please use extension `.ff` for fangs codefiles. \nNot a FANGS codefile but still, running .. .. ..")
    #         with open(os.path.join("scripts", filename), encoding='utf-8') as file:
    #             output = se(filename, ''.join(string.digits + string.ascii_lowercase))
    #             s = Script(file)
    #             s.run()



end = datetime.datetime.now()
print(f" {Colors.cyan}[***] Time taken: [{end - start}]{Colors.reset}")

# if output:
#     print()

#     output.s()
    
#     file_name = output.return_filename()
#     output_result = output.get_data()

#     p_errors = output_result[file_name]["errors"]
#     p_warnings = output_result[file_name]["warnings"]
#     p_success = output_result[file_name]["success"]

#     output.add_e("gfd sgf gdf gsdfg df ")
#     output.add_e("gfd fgfg gsdfg df ")
#     output.add_e("gsgdgg df ")
#     output.add_e("gfd sgf gdf gsdfg df ")
#     output.add_e("gfd sggfdgs df ")
#     output.add_e("gfdgddfg df ")
#     output.add_e("gfd sggdfgfg df ")
#     output.add_e("gfd gfgdfg df ")
#     output.add_e("gfd sgf gdf gsdfg df ")
#     output.add_w("")
#     output.add_s("")
    
#     output.m(f"{Colors.red}ERROR(S)    : (TOTAL: {len(p_errors)}){Colors.reset}")
#     for idx, err in enumerate(p_errors):
#         output.m(f"{Colors.bright_red}{idx+1}{Colors.reset} {err}")

#     output.m(f"{Colors.yellow}WARNING(S)  : (TOTAL: {len(p_warnings)}){Colors.reset}")
#     for idx, warn in enumerate(p_warnings):
#         output.m(f"{Colors.bright_yellow}{idx+1}{Colors.reset} {warn}")

#     output.m(f"{Colors.green}SUCCESS(ES) : (TOTAL: {len(p_success)}){Colors.reset}")
#     for idx, succ in enumerate(p_success):
#         output.m(f"{Colors.bright_green}{idx+1}{Colors.reset} {succ}")

#     output.m(f"Time taken: [{end - start}]")

#     output.delete_json_file()
# else:
#     print("No scripts were executed.")
