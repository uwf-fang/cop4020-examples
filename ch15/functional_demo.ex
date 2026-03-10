# File: functional_demo.ex
defmodule FunctionalDemo do
  # Tail Recursive Factorial with Accumulator
  def factorial(n), do: fact_helper(n, 1)
  defp fact_helper(0, acc), do: acc
  defp fact_helper(n, acc), do: fact_helper(n - 1, n * acc)

  # Apply-to-all (Map)
  def cubic_mapping(list) do
    Enum.map(list, fn x -> x * x * x end)
  end

  # List Comprehension
  def even_cubes(range) do
    for x <- range, rem(x, 2) == 0, do: x * x * x
  end
end

# Execution
IO.puts "Factorial of 5: #{FunctionalDemo.factorial(5)}"
IO.inspect FunctionalDemo.cubic_mapping([1, 2, 3])
IO.inspect FunctionalDemo.even_cubes(1..10)