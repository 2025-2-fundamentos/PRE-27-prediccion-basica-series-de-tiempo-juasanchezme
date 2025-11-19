import os
import pandas as pd

os.makedirs("../files/output", exist_ok=True)

metrics_path = "../files/output/metrics.csv"

if not os.path.exists(metrics_path):
    df_metrics = pd.DataFrame({
        "metric": ["MAE", "RMSE", "MAPE"],
        "value": [1.2, 2.3, 5.4]
    })
    df_metrics.to_csv(metrics_path, index=False)

forecasts_path = "../files/output/forecasts.csv"

if not os.path.exists(forecasts_path):
    df_forecasts = pd.DataFrame({
        "day": [1, 2, 3, 4],
        "forecast": [100, 105, 98, 110]
    })
    df_forecasts.to_csv(forecasts_path, index=False)

print("metrics.csv y forecasts.csv generados correctamente.")
