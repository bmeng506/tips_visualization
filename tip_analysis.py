import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Make sure charts directory exists
os.makedirs("charts", exist_ok=True)

# Load the built-in tips dataset
tips = sns.load_dataset("tips")

print(tips.head())
print(tips.info())
print(tips.describe())

tips["tip_pct"] = tips["tip"] / tips["total_bill"] * 100
print(tips.head())

# 1. Distribution of tip percentage
plt.figure(figsize=(8, 5))
sns.histplot(tips["tip_pct"], bins=30, kde=True)
plt.title("Distribution of Tip Percentage")
plt.xlabel("Tip % of Total Bill")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("charts/tip_pct_distribution.png", dpi=150)
plt.close()

# 2. Tip % by day of week
plt.figure(figsize=(8, 5))
sns.boxplot(data=tips, x="day", y="tip_pct")
plt.title("Tip Percentage by Day of Week")
plt.xlabel("Day")
plt.ylabel("Tip %")
plt.tight_layout()
plt.savefig("charts/tip_pct_by_day.png", dpi=150)
plt.close()

# 3. Weekday vs weekend
tips["is_weekend"] = tips["day"].isin(["Sat", "Sun"])

plt.figure(figsize=(6, 5))
sns.boxplot(data=tips, x="is_weekend", y="tip_pct")
plt.xticks([0, 1], ["Weekday", "Weekend"])
plt.title("Tip Percentage: Weekday vs Weekend")
plt.xlabel("")
plt.ylabel("Tip %")
plt.tight_layout()
plt.savefig("charts/tip_pct_weekday_weekend.png", dpi=150)
plt.close()

# 4. Lunch vs dinner
plt.figure(figsize=(6, 5))
sns.boxplot(data=tips, x="time", y="tip_pct")
plt.title("Tip Percentage at Lunch vs Dinner")
plt.xlabel("Meal")
plt.ylabel("Tip %")
plt.tight_layout()
plt.savefig("charts/tip_pct_by_meal.png", dpi=150)
plt.close()

# 5. Tip % vs party size
plt.figure(figsize=(8, 5))
sns.scatterplot(data=tips, x="size", y="tip_pct", alpha=0.7)
sns.lineplot(
    data=tips.groupby("size", as_index=False)["tip_pct"].mean(),
    x="size", y="tip_pct", marker="o"
)
plt.title("Tip Percentage vs Party Size")
plt.xlabel("Party Size")
plt.ylabel("Tip %")
plt.tight_layout()
plt.savefig("charts/tip_pct_vs_party_size.png", dpi=150)
plt.close()

# 6. Tip vs total bill (color = tip %, size = party size)
plt.figure(figsize=(8, 6))
scatter = sns.scatterplot(
    data=tips,
    x="total_bill",
    y="tip",
    hue="tip_pct",
    size="size",
    alpha=0.8
)
plt.title("Tip vs Total Bill\nColor = Tip %, Size = Party Size")
plt.xlabel("Total Bill ($)")
plt.ylabel("Tip ($)")
plt.legend(bbox_to_anchor=(1.05, 1), loc="upper left")
plt.tight_layout()
plt.savefig("charts/tip_vs_total_bill.png", dpi=150)
plt.close()

# 7. Summary: avg tip % by day and meal
summary = (
    tips.groupby(["day", "time"], observed=True)
        .agg(
            avg_tip_pct=("tip_pct", "mean"),
            avg_bill=("total_bill", "mean"),
        )
        .reset_index()
)

plt.figure(figsize=(8, 5))
sns.barplot(data=summary, x="day", y="avg_tip_pct", hue="time")
plt.title("Average Tip % by Day and Meal")
plt.xlabel("Day of Week")
plt.ylabel("Average Tip %")
plt.tight_layout()
plt.savefig("charts/avg_tip_pct_by_day_meal.png", dpi=150)
plt.close()

print(summary.sort_values("avg_tip_pct", ascending=False))
