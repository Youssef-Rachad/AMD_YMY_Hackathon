# frozen_string_literal: true

Gem::Specification.new do |spec|
    spec.name          = "ymy"
    spec.version       = "0.0.0"
    spec.authors       = ["Youssef Rachad", "Matthew Oliveira", "Youssef El Mays"]
    spec.email         = [""]
    spec.license       = ""
    spec.homepage      = "https://github.com/Youssef-Rachad/AMD_YMY_Hackathon"
    spec.summary       = "Hackathon Source for the Best ChatGPT x CodeQL Util."
  
    spec.license       = " "
    spec.files         = `git ls-files -z`.split("\x0").select { |f| f.match(%r!^website/(assets|_data|_layouts|_includes|_sass|LICENSE|README|_config\.yml)!i) }
  
    spec.add_runtime_dependency "jekyll", "~> 4.3"
  end