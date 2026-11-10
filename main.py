"""Лавка Архивариуса — мини-симулятор магазина (Python RPG, уровень 0).
Автор: Пономарев Егор Алексеевич
"""
import sys

# Коллекция dict: название товара -> цена в золотых
PRICES = {
    "зелье": 10,
    "меч": 50,
    "щит": 40,
    "карта": 15,
}


def buy(gold, inventory, item):
    """Покупает товар. Возвращает (новое_золото, сообщение)."""
    if item not in PRICES:
        return gold, f"Такого товара нет: «{item}»."
    price = PRICES[item]
    if gold < price:
        return gold, f"Не хватает золота: нужно {price}, у тебя {gold}."
    inventory.append(item)  # коллекция list: рюкзак героя
    return gold - price, f"Куплено: {item} за {price} зол."


def sell(gold, inventory, item):
    """Продаёт товар из рюкзака за половину цены. Возвращает (новое_золото, сообщение)."""
    if item not in inventory:
        return gold, f"В рюкзаке нет предмета «{item}»."
    inventory.remove(item)
    income = PRICES[item] // 2
    return gold + income, f"Продано: {item} за {income} зол."


def show_inventory(inventory):
    """Возвращает строку с содержимым рюкзака (с подсчётом одинаковых предметов)."""
    if not inventory:
        return "Рюкзак пуст."
    counts = {}
    for item in inventory:
        counts[item] = counts.get(item, 0) + 1
    return ", ".join(f"{name} x{n}" for name, n in counts.items())


def show_prices():
    return "\n".join(f"  {name} — {price} зол." for name, price in PRICES.items())


def run_tests():
    """Автоматические проверки (assert): python main.py --test"""
    inv = []
    # обычный сценарий
    gold, _ = buy(100, inv, "меч")
    assert gold == 50 and inv == ["меч"]
    # граничный: не хватает золота
    gold, _ = buy(5, inv, "щит")
    assert gold == 5 and inv == ["меч"]
    # неизвестный товар
    gold, _ = buy(100, inv, "дракон")
    assert gold == 100
    # продажа
    gold, _ = sell(50, inv, "меч")
    assert gold == 75 and inv == []
    # продажа отсутствующего предмета
    gold, _ = sell(10, inv, "меч")
    assert gold == 10
    assert show_inventory([]) == "Рюкзак пуст."
    assert show_inventory(["зелье", "зелье"]) == "зелье x2"
    print("Все проверки пройдены.")


def main():
    gold = 100
    inventory = []
    print("=== Лавка Архивариуса ===")
    while True:
        print(f"\nЗолото: {gold}")
        print("1 — товары | 2 — купить | 3 — продать | 4 — рюкзак | 0 — выход")
        choice = input("Выбор: ").strip()
        if choice == "1":
            print(show_prices())
        elif choice == "2":
            gold, msg = buy(gold, inventory, input("Что купить? ").strip().lower())
            print(msg)
        elif choice == "3":
            gold, msg = sell(gold, inventory, input("Что продать? ").strip().lower())
            print(msg)
        elif choice == "4":
            print(show_inventory(inventory))
        elif choice == "0":
            print("Удачи в Гильдии!")
            break
        else:
            print("Неизвестная команда, введи число от 0 до 4.")


if __name__ == "__main__":
    if "--test" in sys.argv:
        run_tests()
    else:
        main()
