import os
import traceback

def main() -> None:
    path = None
    while True:
        path = input("Enter the path of SpaceEngineers (ex. E:\Steam\steamapps\common\SpaceEngineers): ")
        if not path or path == "\n":
            print("[ERROR] You havent entered anything...")
            continue

        if not os.path.exists(path):
            print('[ERROR] Couldnt find this path...')
            continue

        break

    if not path:
        return
    
    sbcs_path = os.path.join(path, "Content", "Data", "CubeBlocks")
    if not os.path.exists(sbcs_path):
        print(f"[ERROR] Could not find: {sbcs_path}")
        return
    
    sbcs = os.listdir(sbcs_path)

    if not sbcs:
        print(f"[ERROR] No files in {sbcs_path} found!")
        return
    
    for sbc in sbcs:
        if not sbc.endswith(".sbc"):
            continue

        full_path = os.path.join(sbcs_path, sbc)

        lines = None

        try:
            with open(full_path, encoding='utf-8') as file:
                lines = file.read().splitlines()
        except:
            print(traceback.format_exc())
            continue

        if not lines:
            continue

        new_lines = []

        for line in lines:
            line = str(line)
            if "<DLC>" in line and "</DLC>" in line:
                continue

            new_lines.append(line)

        try:
            with open(full_path, "w", encoding='utf-8') as file:
                for val, line in enumerate(new_lines):
                    if val == 0:
                        file.write(line)
                    else:
                        file.write("\n" + line)
        except:
            print(traceback.format_exc())
            continue

if __name__ == "__main__":
    main()