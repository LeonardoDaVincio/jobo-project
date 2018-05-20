using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.DependencyInjection;
using System;
using System.Collections.Generic;
using System.Linq;

namespace Bojo_Frontend.Entities
{
    public static class SeedData
    {
        public static void Initialize(IServiceProvider serviceProvider)
        {
            using (var context = new BojoContext(
                serviceProvider.GetRequiredService<DbContextOptions<BojoContext>>()))
            {
                context.Database.ExecuteSqlCommand("DELETE FROM Temperatures");
                var temps = new List<Temperature>();
                var time = DateTime.Now;
                decimal temp = -10;
                for (var i = 0; i < 1000; i++)
                {
                    temps.Add(new Temperature()
                    {
                        TempSensor = "First",
                        Temp = temp + 1 * (decimal)Math.Sin((double)temp),
                        Time = time
                    });
                    temps.Add(new Temperature()
                    {
                        TempSensor = "Second",
                        Temp = temp + 2 * (decimal)Math.Sin((double)temp),
                        Time = time
                    });
                    temps.Add(new Temperature()
                    {
                        TempSensor = "Third",
                        Temp = temp + 4 * (decimal)Math.Sin((double)temp),
                        Time = time
                    });
                    temps.Add(new Temperature()
                    {
                        TempSensor = "Set",
                        Temp = RectangularFunction(temp),
                        Time = time
                    });
                    time = time.AddSeconds(1);
                    temp += (decimal)0.1;
                }
                context.Temperatures.AddRange(temps);
                context.SaveChanges();
            }
        }

        private static decimal RectangularFunction(decimal input)
        {
            int sign = input >= 0 ? 1 : -1;
            int size = (int)Math.Abs(input) / 2;
            int output = sign * size * 3;
            return (decimal)output;

        }
    }
}