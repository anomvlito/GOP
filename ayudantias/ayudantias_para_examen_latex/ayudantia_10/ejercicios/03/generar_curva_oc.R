n <- 99
c <- 4
aql <- 0.02
lptd <- 0.08

p <- seq(0, 0.14, by = 0.0005)
pa <- pbinom(c, size = n, prob = p)

pa_aql <- pbinom(c, size = n, prob = aql)
pa_lptd <- pbinom(c, size = n, prob = lptd)

png("figuras/curva_oc_muestreo.png", width = 1400, height = 850, res = 160)
par(mar = c(4.8, 5.0, 3.0, 1.0))
plot(p, pa, type = "l", lwd = 2.5, col = "#1F4E79",
     xlab = "Fraccion defectuosa real del lote (p)",
     ylab = "Probabilidad de aceptar el lote Pa(p)",
     main = "Curva OC del plan de muestreo (n = 99, c = 4)",
     ylim = c(0, 1), xlim = c(0, 0.14))
grid(col = "#D9D9D9", lty = 1)
abline(v = aql, col = "#006400", lwd = 2, lty = 2)
abline(v = lptd, col = "#A00000", lwd = 2, lty = 2)
abline(h = 0.95, col = "#006400", lwd = 1.8, lty = 3)
abline(h = 0.10, col = "#A00000", lwd = 1.8, lty = 3)
points(c(aql, lptd), c(pa_aql, pa_lptd),
       pch = 19, cex = 1.35, col = c("#006400", "#A00000"))
text(aql + 0.012, pa_aql - 0.06,
     labels = "AQL = 0.02\nPa = 0.9509\nalpha = 0.0491",
     col = "#006400", cex = 0.9)
text(lptd + 0.018, pa_lptd + 0.08,
     labels = "LPTD = 0.08\nPa = 0.0948\nbeta = 0.0948",
     col = "#A00000", cex = 0.9)
legend("topright",
       legend = c("Curva OC", "AQL: lote bueno", "LPTD: lote malo"),
       col = c("#1F4E79", "#006400", "#A00000"),
       lty = c(1, 2, 2), lwd = c(2.5, 2, 2),
       bty = "n")
dev.off()
