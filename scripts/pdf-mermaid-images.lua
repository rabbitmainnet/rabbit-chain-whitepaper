local diagram_index = 0
local files = {
  "assets/diagrams/mining-lcq-flow.png",
  "assets/diagrams/lcq-liveness-flow.png",
  "assets/diagrams/rab-allocation-transparency.png"
}

function CodeBlock(block)
  if block.classes:includes("mermaid") then
    diagram_index = diagram_index + 1
    if diagram_index == 3 then
      return pandoc.Div({
        pandoc.Para({pandoc.Strong("15,000,000 RAB genesis allocation")}),
        pandoc.BulletList({
          {pandoc.Plain("10,000,000 RAB staking/participation genesis reserve, separate from block rewards")},
          {pandoc.Plain("5,000,000 RAB at precomputed contract addresses; verified contracts are deployed in the first mainnet blocks")},
          {pandoc.Plain("Consensus issuance: 1.20 -> 0.60 -> 0.30 -> 0.15 RAB per block")},
          {pandoc.Plain("Permanent tail emission: 0.15 RAB per block")}
        })
      })
    end
    return pandoc.Para({pandoc.Image("Rabbit Chain diagram", files[diagram_index])})
  end
end

function Table(tbl)
  local count = #tbl.colspecs
  local widths = nil
  if count == 2 then
    widths = {0.38, 0.62}
  elseif count == 3 then
    widths = {0.20, 0.35, 0.45}
  elseif count == 4 then
    widths = {0.16, 0.20, 0.28, 0.36}
  end
  if widths then
    for i = 1, count do
      tbl.colspecs[i][2] = widths[i]
    end
  end
  return tbl
end
