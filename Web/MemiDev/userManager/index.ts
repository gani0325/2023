import {createInterface} from 'node:readline';
import { stdin, stdout} from "node:process";
import fs from "node:fs/promises";
const rl = createInterface(stdin);
const p = console.log;

interface User {
    name: string,
    age: number,
    hobbies: string[]
};

class UserManager {
    private users: User[] = []
    constructor () {
        // this.users = []
    }

    // 1) 정보 추가하기
    private add (name: string, age: number, hobbies?: string[]) {
        this.users.push({name, age, hobbies: hobbies || []})
    }
    // 2) 정보 제거하기
    private remove(name: string) {
        const index = this.users.findIndex((v) => v.name === name)
        if (index < 0) throw Error ("no users!")
        this.users.splice(index, 1)
    }

    // 3) 정보 출력하기
    get list () {
      return this.users.map(v => `${v.name} ${v.age} ${v.hobbies.join(",")}`).join("\n")
    }

    // 4) 정보 저장하기
    async save () {
      const buf = JSON.stringify(this.users)
      await fs.writeFile("users.json", buf)
    }

    // 5) 정보 불러오기
    async load () {
      const buf = await fs.readFile("users.json")
      this.users = JSON.parse(buf.toString())
      return "loaded"
    }
    async execute (l: string) {
            // =====> p("추가하기", splitInput);
            // add gani 12 cook,cut
            // 추가하기 [ 'add', 'gani', '12', 'cook,cut' ]
            // rm  12
            // 추가하기 [ 'rm', '', '12' ]
        // add user 12 cook,cut => 파싱하기
        // rm user
        const splitInput = l.split(" ");
        const command = splitInput.shift();
        let message = "done";

        switch (command) {
            case "add" :
                {
                  const name = splitInput.shift();
                  if (!name) throw Error("no name");

                  const age = Number(splitInput.shift());
                  if (!age) throw Error("no age");

                  const every = splitInput.shift();
                  every ? this.add(name, age, every.split(",")) : this.add(name, age)
                  p(this.users);
                  message = "Successfully added"
                }
                break

            case "rm" :
                {
                  const name = splitInput.shift();
                  if (!name) throw Error("no name")
                  this.remove(name)
                  message = "Successfully removed"
                }
                break

            case "ls" :
              {
                message = this.list
                break
              }

            case "save" :
              await this.save()
              break

            case "load" :
              await this.load()
              break

            default :
            p("unknown command")
            break
        };
        return message;
    }
}

const userManager = new UserManager();
  userManager.load()
    .then(r => p(r))
    .catch(e => p(e.message))
  rl.on("line", (l) => {
    userManager
      .execute(l)
      .then(r => p(r))
      .catch(e => p(e.message))
})