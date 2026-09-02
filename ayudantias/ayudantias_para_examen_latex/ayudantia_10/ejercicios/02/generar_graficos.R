x <- c(342, 356, 381, 322, 355, 359, 368, 341, 333,
       342, 366, 371, 340, 370, 365, 354, 353, 326,
       376, 320, 359, 378, 397, 319, 347, 374, 324)
muestra <- seq_along(x)

out_agregado <- c(23, 24)
media <- 9538 / 27
sigma <- sqrt(3376759 / 27 - media^2)
z <- 2.055
lci <- media - z * sigma
lcs <- media + z * sigma

png("figuras/control_inicial.png", width = 1400, height = 850, res = 160)
par(mar = c(4.5, 4.5, 3, 1))
plot(muestra, x, type = "b", pch = 19, lwd = 1.4,
     xlab = "Muestra", ylab = "Peso (g)",
     main = "Carta de control inicial",
     ylim = c(300, 405), xaxt = "n")
axis(1, at = muestra)
abline(h = media, col = "#1F4E79", lwd = 2)
abline(h = lcs, col = "#A00000", lwd = 2, lty = 2)
abline(h = lci, col = "#A00000", lwd = 2, lty = 2)
points(out_agregado, x[out_agregado], pch = 19, col = "#A00000", cex = 1.4)
text(out_agregado, x[out_agregado] + c(4, -5), labels = out_agregado,
     col = "#A00000", font = 2)
legend("topleft",
       legend = c("Peso observado", "Media", "Limites 96%", "Fuera de control"),
       col = c("black", "#1F4E79", "#A00000", "#A00000"),
       lty = c(1, 1, 2, NA), pch = c(19, NA, NA, 19),
       bty = "n")
dev.off()

x_limpio <- x[-out_agregado]
muestra_limpia <- muestra[-out_agregado]
suma_limpia <- 9538 - x[23] - x[24]
suma2_limpia <- 3376759 - x[23]^2 - x[24]^2
media_limpia <- suma_limpia / length(x_limpio)
sigma_limpia <- sqrt(suma2_limpia / length(x_limpio) - media_limpia^2)
lci_limpio <- media_limpia - z * sigma_limpia
lcs_limpio <- media_limpia + z * sigma_limpia
out_recalculado <- muestra_limpia[x_limpio < lci_limpio | x_limpio > lcs_limpio]

png("figuras/control_recalculado.png", width = 1400, height = 850, res = 160)
par(mar = c(4.5, 4.5, 3, 1))
plot(muestra_limpia, x_limpio, type = "b", pch = 19, lwd = 1.4,
     xlab = "Muestra original", ylab = "Peso (g)",
     main = "Carta de control recalculada sin muestras 23 y 24",
     ylim = c(300, 405), xaxt = "n")
axis(1, at = muestra)
abline(h = media_limpia, col = "#1F4E79", lwd = 2)
abline(h = lcs_limpio, col = "#006400", lwd = 2, lty = 2)
abline(h = lci_limpio, col = "#006400", lwd = 2, lty = 2)
if (length(out_recalculado) > 0) {
  points(out_recalculado, x[out_recalculado], pch = 19, col = "#A00000", cex = 1.4)
  text(out_recalculado, x[out_recalculado] + 4, labels = out_recalculado,
       col = "#A00000", font = 2)
}
legend("topleft",
       legend = c("Peso observado", "Media recalculada", "Limites recalculados", "Fuera de control"),
       col = c("black", "#1F4E79", "#006400", "#A00000"),
       lty = c(1, 1, 2, NA), pch = c(19, NA, NA, 19),
       bty = "n")
dev.off()
