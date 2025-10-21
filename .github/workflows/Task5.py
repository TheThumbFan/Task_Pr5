// password-generator.js

const readline = require("readline");

// Функція генерації пароля
function genPass(length = 12, level = "Середній") {
  let chars = "";
  if (level === "Легкий") {
    chars = "abcdefghijklmnopqrstuvwxyz0123456789";
  } else if (level === "Середній") {
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
  } else if (level === "Складний") {
    chars =
      "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*";
  } else {
    throw new Error("Рівень має бути: Легкий, Середній або Складний");
  }

  let password = "";
  for (let i = 0; i < length; i++) {
    password += chars.charAt(Math.floor(Math.random() * chars.length));
  }
  return password;
}

// Інтерфейс для консолі
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

function mainMenu() {
  console.log("\n" + "=".repeat(45));
  console.log("                 ГОЛОВНЕ МЕНЮ");
  console.log("=".repeat(45));
  console.log("1. Згенерувати легкий пароль (8 символів)");
  console.log("2. Згенерувати середній пароль (12 символів)");
  console.log("3. Згенерувати складний пароль (16 символів)");
  console.log("4. Вихід");
  console.log("5. Інформація про автора");
  console.log("6. Інформація про програму");
  console.log("7. Теоретичний матеріал");
  console.log("=".repeat(45));
  console.log("Для вибору натисніть число від 1 до 7");
  console.log("=".repeat(45));

  rl.question("Ваш вибір: ", (choice) => {
    switch (choice) {
      case "1":
        console.log("\n--- Результат ---");
        console.log("Ви обрали: Легкий пароль");
        console.log("Ваш пароль:", genPass(8, "Легкий"));
        break;
      case "2":
        console.log("\n--- Результат ---");
        console.log("Ви обрали: Середній пароль");
        console.log("Ваш пароль:", genPass(12, "Середній"));
        break;
      case "3":
        console.log("\n--- Результат ---");
        console.log("Ви обрали: Складний пароль");
        console.log("Ваш пароль:", genPass(16, "Складний"));
        break;
      case "4":
        console.log("\nДякую за використання програми. До зустрічі!");
        rl.close();
        return;
      case "5":
        console.log("\n--- Автор ---");
        console.log("Автор програмного модуля: Мельниченко Владислав");
        console.log("Email: [Ваш email тут]");
        break;
      case "6":
        console.log("\n--- Про програму ---");
        console.log("Це консольний додаток для генерації випадкових паролів.");
        console.log("Доступні рівні складності: легкий, середній, складний.");
        break;
      case "7":
        console.log("\n--- Теоретичний матеріал ---");
        console.log("1. Програма використовує Math.random() для випадкових символів.");
        console.log("2. Користувач обирає рівень складності (легкий, середній, складний).");
        console.log("3. Залежно від рівня формується набір символів:");
        console.log("   - Легкий: маленькі букви + цифри");
        console.log("   - Середній: великі та маленькі букви + цифри");
        console.log("   - Складний: букви + цифри + спецсимволи (!@#$%^&*)");
        console.log("4. Генерується пароль потрібної довжини.");
        break;
      default:
        console.log("\nНеправильний вибір. Спробуйте ще раз.");
    }

    rl.question("\nНатисніть Enter, щоб повернутися в головне меню...", () => {
      mainMenu();
    });
  });
}

// Запуск програми
mainMenu();
