local function rabbit_image(path, alt)
  return pandoc.Para({pandoc.Image(alt, path)})
end

function CodeBlock(block)
  if not block.classes:includes("mermaid") then
    return nil
  end

  local text = block.text or ""

  if text:find("Wallet and synchronized client", 1, true) then
    return rabbit_image("assets/diagrams/mining-lcq-flow.png", "Rabbit Work V2 admission and LCQ")
  end

  if text:find("Canonical producer slot", 1, true) then
    return rabbit_image("assets/diagrams/lcq-liveness-flow.png", "Rabbit LCQ liveness and permissionless recovery")
  end

  if text:find("15,000,000 RAB genesis allocation", 1, true) then
    return rabbit_image("assets/diagrams/rab-allocation-transparency.png", "Rabbit Chain genesis allocation transparency")
  end

  return nil
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
