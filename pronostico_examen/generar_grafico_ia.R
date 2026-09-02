set.seed(3213)

horas <- seq(0.5, 8, length.out = 34)
dominio <- 43 + 7.4 * horas - 0.36 * horas^2 + rnorm(length(horas), 0, 4.2)
dominio <- pmin(100, pmax(35, dominio))

argumentos <- commandArgs(trailingOnly = FALSE)
archivo_script <- sub("^--file=", "", argumentos[grep("^--file=", argumentos)])
directorio_script <- if (length(archivo_script)) dirname(normalizePath(archivo_script)) else getwd()
salida <- file.path(directorio_script, "figuras", "potencial_ia.pdf")
dir.create(dirname(salida), recursive = TRUE, showWarnings = FALSE)

cairo_pdf(salida, width = 7.2, height = 2.35, family = "sans")
par(
  mar = c(3.1, 3.8, 1.0, 0.6),
  mgp = c(1.8, 0.55, 0),
  tcl = -0.22,
  las = 1,
  cex.axis = 0.72,
  cex.lab = 0.82,
  fg = "#5A5A5A",
  col.axis = "#5A5A5A",
  col.lab = "#1F4E79"
)

plot(
  horas, dominio,
  xlab = "Horas de estudio focalizado con apoyo de IA",
  ylab = "Dominio esperado (%)",
  xlim = c(0, 8.4), ylim = c(35, 100),
  pch = 21, bg = adjustcolor("#4682B4", 0.58), col = "white", cex = 1.12,
  bty = "n"
)
abline(h = seq(40, 100, 20), col = "#E4EAF0", lwd = 0.8)
points(
  horas, dominio,
  pch = 21, bg = adjustcolor("#4682B4", 0.65), col = "white", cex = 1.12
)

ajuste <- loess(dominio ~ horas, span = 0.72)
x_pred <- seq(min(horas), max(horas), length.out = 200)
y_pred <- predict(ajuste, newdata = data.frame(horas = x_pred))
lines(x_pred, y_pred, col = "#006400", lwd = 2.4)

text(5.9, 91.5, "La IA amplifica; la práctica consolida", col = "#006400", cex = 0.78, font = 2)
mtext("Ilustración conceptual con datos sintéticos", side = 1, line = 2.25, cex = 0.62, col = "#777777")
dev.off()
