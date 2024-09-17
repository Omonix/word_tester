let tab_info = [
  { name: "test", trad: "tester" },
  { name: "hola", trad: "hello" },
];

const lb_joinElement = (e) => {
  let result = "";
  for (let i = 0; i < e.length; i++) {
    if (i !== e.length - 1) {
      result += e[i] + "\n";
    } else {
      result += e[i];
    }
  }
  return result;
};
const lb_upper_0 = (word) => {
  return word[0].toUpperCase() + word.substring(1, word.length).toLowerCase();
};
const lb_createElement = (type, classer, value, index) => {
  const e = document.createElement(type);
  e.className = classer;
  e.innerHTML = value;
  e.id = index;
  return e;
};
const lb_tester = (questions) => {
  let controler = [].concat(questions);
  for (let i = 0; i < questions.length; i++) {
    let x = Math.floor(Math.random() * controler.length);
    let element = controler[x].name;
    document
      .querySelector(".inputs")
      .appendChild(lb_createElement("div", "questionDiv", "", i));
    if (i === 0) {
      document
        .querySelector(".questionDiv")
        .appendChild(
          lb_createElement("div", "whats", `${lb_upper_0(element)} ?`, i)
        );
      document
        .querySelector(".questionDiv")
        .appendChild(lb_createElement("input", "answer", "", i));
    } else {
      document
        .querySelectorAll(".questionDiv")
        [i].appendChild(
          lb_createElement("div", "whats", `${lb_upper_0(element)} ?`, i)
        );
      document
        .querySelectorAll(".questionDiv")
        [i].appendChild(lb_createElement("input", "answer", "", i));
    }
    controler.splice(x, 1);
  }
  return;
};
document.querySelector(".submit").addEventListener("click", () => {
  let arr_answer = [];
  let arr_trueAnswer = [];
  for (let i = 0; i < document.querySelectorAll(".answer").length; i++) {
    arr_answer.push(document.querySelectorAll(".answer")[i].value);
  }
  arr_answer.forEach((e, i) => {
    let boolar = "";
    if (e.toLowerCase() === tab_info[i].trad) {
      boolar = "TRUE";
    } else {
      boolar = "FALSE";
    }
    arr_trueAnswer.push(
      `${boolar} / ${lb_upper_0(tab_info[i].name)} : ${lb_upper_0(
        tab_info[i].trad
      )}`
    );
  });
  console.log(lb_joinElement(arr_trueAnswer));
});

lb_tester(tab_info);
