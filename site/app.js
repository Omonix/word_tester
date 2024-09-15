const upper_0 = (word) => {
  return word[0].toUpperCase() + word.substring(1, word.length).toLowerCase();
};
const createElement = (type, classer, value, index) => {
  const e = document.createElement(type);
  e.className = classer;
  e.value = value;
  e.id = index;
  return e;
};
const tester = (questions) => {
  result = "";
  for (let i = 0; i < questions.length; i++) {
    document
      .querySelector(".inputs")
      .appendChild(createElement("div", "test", "Hello", i));
    x = Math.floor(Math.random() * questions.length);
    element = questions[x].name;
    console.log(`${upper_0(element)} ? `);
  }
  return result;
};
console.log(
  tester([
    { name: "test", trad: "tester" },
    { name: "hola", trad: "hello" },
  ])
);
