import std;

namespace nagisa::algorithm::sort
{
	template<bool Stable>
	struct sort_trait_base
	{
		constexpr static auto stable_sort = Stable;
	};

	inline constexpr struct select_by_swap_t : sort_trait_base<false>
	{
		template<class Predicate = ::std::ranges::less, class Project = ::std::identity>
		constexpr decltype(auto) operator()(
			::std::ranges::forward_range auto&& range,
			Predicate predicate = {},
			Project project = {}
			) const noexcept
			requires ::std::sortable<::std::ranges::iterator_t<decltype(range)>, Predicate, Project>
		{
			for (auto i = ::std::ranges::begin(range); i != ::std::ranges::end(range); ++i)
			{
				::std::ranges::iter_swap(i, ::std::ranges::min_element(i, ::std::ranges::end(range), predicate, project));
			}
		}
	}select{};

	inline constexpr struct bubble_t : sort_trait_base<true>
	{
		template<class Predicate = ::std::ranges::less, class Project = ::std::identity>
		constexpr decltype(auto) operator()(
			::std::ranges::forward_range auto&& range,
			Predicate predicate = {},
			Project project = {}
			) const noexcept
			requires ::std::sortable<::std::ranges::iterator_t<decltype(range)>, Predicate, Project>
		{
			if (::std::ranges::empty(range))
				return;
			auto flag = true;
			while (flag)
			{
				flag = false;
				for (auto it = ::std::ranges::begin(range); ::std::ranges::next(it) != ::std::ranges::end(range); ++it)
				{
					if (::std::invoke(predicate, ::std::invoke(project, *it), ::std::invoke(project, *::std::ranges::next(it))))
						continue;
					flag = true;
					::std::ranges::iter_swap(it, ::std::ranges::next(it));
				}
			}
		}
	}bubble{};

	inline constexpr struct insert_t : sort_trait_base<true>
	{
		template<class Predicate = ::std::ranges::less, class Project = ::std::identity>
		constexpr decltype(auto) operator()(
			::std::ranges::forward_range auto&& range,
			Predicate predicate = {},
			Project project = {}
			) const noexcept
			requires ::std::sortable<::std::ranges::iterator_t<decltype(range)>, Predicate, Project>
		{
			for (auto i = ::std::ranges::begin(range); i != ::std::ranges::end(range); ++i)
			{
				::std::ranges::rotate(
					::std::ranges::upper_bound(::std::ranges::begin(range), i, ::std::invoke(project, *i), predicate, project),
					i,
					::std::ranges::next(i)
				);
			}
		}
	}insert{};

	inline constexpr struct count_t : sort_trait_base<true>
	{
		template<class Predicate = ::std::ranges::less, class Project = ::std::identity>
		constexpr decltype(auto) operator()(
			::std::ranges::forward_range auto&& range,
			Predicate predicate = {},
			Project project = {}
			) const noexcept
			requires ::std::sortable<::std::ranges::iterator_t<decltype(range)>, Predicate, Project>
		{

		}
	}count{};

	inline constexpr struct quick_t : sort_trait_base<false>
	{
		template<class Predicate = ::std::ranges::less, class Project = ::std::identity>
		constexpr void operator()(
			::std::ranges::forward_range auto&& range,
			Predicate predicate = {},
			Project project = {}
			) const noexcept
			requires ::std::sortable<::std::ranges::iterator_t<decltype(range)>, Predicate, Project>
		{
			if (::std::ranges::empty(range))
				return;
			auto result = ::std::ranges::begin(range);
			for (auto it = ::std::ranges::begin(range); it != ::std::ranges::end(range);)
			{
				::std::ranges::iterator_t<decltype(range)> right;
				{
					auto found = ::std::ranges::find_last_if_not(::std::ranges::next(it), ::std::ranges::end(range),
						[it, predicate, project](auto const& r) noexcept { return ::std::invoke(predicate, ::std::invoke(project, *it), r); },
						project
					);
					if (::std::ranges::empty(found))
					{
						result = it;
						break;
					}
					right = ::std::ranges::begin(found);
					::std::ranges::iter_swap(it, right);
				}
				it = ::std::ranges::next(it);
				{
					auto found = ::std::ranges::find_if_not(it, right,
						[right, predicate, project](auto const& l) noexcept { return ::std::invoke(predicate, l, ::std::invoke(project, *right)); },
						project
					);
					if (found == right)
					{
						result = right;
						break;
					}
					it = found;
					::std::ranges::iter_swap(it, right);
				}
			}
			this->operator()(::std::ranges::subrange(::std::ranges::begin(range), result), predicate, project);
			this->operator()(::std::ranges::subrange(::std::ranges::next(result), ::std::ranges::end(range)), predicate, project);
		}
	}quick{};
}


struct particle
{
	::std::string name; double mass; // MeV
};

template<>
struct ::std::formatter<particle, char>
{
	constexpr static auto parse(auto& context) noexcept
	{
		return ::std::ranges::next(::std::ranges::begin(context), ::std::ranges::end(context));
	}

	constexpr static auto format(particle const& p, auto& context) noexcept
	{
		return ::std::ranges::copy(::std::format("{}: {}", p.name, p.mass), context.out()).out;
	}
};

int main()
{
	::std::array s{ 5, 7, 4, 2, 8, 6, 1, 9, 0, 3 };

	constexpr auto sort = ::nagisa::algorithm::sort::quick;


	sort(s);
	::std::println("以默认 operator< 排序 {}", s);

	sort(s, ::std::ranges::greater());
	::std::println("以标准库比较函数对象排序 {}", s);

	struct
	{
		bool operator()(int a, int b) const { return a < b; }
	} customLess;
	sort(s, customLess);
	::std::println("以自定义函数对象排序 {}", s);

	sort(s, [](int a, int b) { return a > b; });
	::std::println("以 lambda 表达式排序 {}", s);

	auto particles = ::std::array
	{
		particle{"Electron", 0.511}, particle{"Muon", 105.66}, particle{"Tau", 1776.86},
		particle{"Positron", 0.511}, particle{"Proton", 938.27}, particle{"Neutron", 939.57}
	};
	sort(particles, {}, &particle::name);
	::std::println("以投影按名字排序 {}", particles);
	sort(particles, {}, &particle::mass);
	::std::println("以投影按质量排序 {}", particles);
}